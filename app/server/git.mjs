// Git integration for the concept editor backend.
//
// The browser cannot talk to git directly, so it POSTs its accumulated Turtle
// additions here and this module commits + pushes them to the configured
// repository. In a deployed container the repo is cloned on first use from
// GIT_REMOTE_URL using GIT_TOKEN; in local dev it operates on the checked-out
// repo at REPO_DIR.

import { simpleGit } from 'simple-git';
import { promises as fs } from 'node:fs';
import path from 'node:path';

const cfg = {
  repoDir: process.env.REPO_DIR || path.resolve(process.cwd(), '..'),
  remoteUrl: process.env.GIT_REMOTE_URL || '',
  token: process.env.GIT_TOKEN || '',
  branch: process.env.GIT_BRANCH || 'concept-edits',
  remote: process.env.GIT_REMOTE || 'origin',
  editsPath: process.env.EDITS_PATH || '_sources/oim-variables/edits',
  authorName: process.env.GIT_AUTHOR_NAME || 'SeaDOTs Concept Editor',
  authorEmail: process.env.GIT_AUTHOR_EMAIL || 'concept-editor@seadots.eu',
  push: (process.env.GIT_PUSH ?? 'true') !== 'false',
};

/** Inject the token into an https remote URL for non-interactive push. */
function authedUrl(url, token) {
  if (!token || !url.startsWith('https://')) return url;
  return url.replace('https://', `https://x-access-token:${token}@`);
}

async function isGitRepo(dir) {
  try {
    await fs.access(path.join(dir, '.git'));
    return true;
  } catch {
    return false;
  }
}

/** Ensure REPO_DIR is a usable clone; clone it if a remote URL was provided. */
async function ensureRepo() {
  if (await isGitRepo(cfg.repoDir)) return simpleGit(cfg.repoDir);
  if (!cfg.remoteUrl) {
    throw new Error(
      `REPO_DIR (${cfg.repoDir}) is not a git repo and no GIT_REMOTE_URL set to clone from.`,
    );
  }
  await fs.mkdir(cfg.repoDir, { recursive: true });
  const git = simpleGit();
  await git.clone(authedUrl(cfg.remoteUrl, cfg.token), cfg.repoDir);
  return simpleGit(cfg.repoDir);
}

/**
 * Commit a Turtle payload and push it.
 * @param {{turtle: string, message: string, filename?: string}} input
 * @returns {Promise<{commit: string, branch: string, file: string, pushed: boolean}>}
 */
export async function commitTurtle({ turtle, message, filename }) {
  if (!turtle || !turtle.trim()) throw new Error('No Turtle content to commit.');
  const git = await ensureRepo();

  await git.addConfig('user.name', cfg.authorName);
  await git.addConfig('user.email', cfg.authorEmail);

  // Move onto the working branch, refreshed from the remote when possible.
  await git.fetch(cfg.remote).catch(() => {});
  const branches = await git.branchLocal();
  if (branches.all.includes(cfg.branch)) {
    await git.checkout(cfg.branch);
  } else {
    await git.checkoutLocalBranch(cfg.branch);
  }

  const safeName =
    (filename || `concept-edit-${new Date().toISOString().replace(/[:.]/g, '-')}`).replace(
      /[^\w.-]/g,
      '_',
    );
  const relFile = path.join(cfg.editsPath, `${safeName}.ttl`);
  const absFile = path.join(cfg.repoDir, relFile);
  await fs.mkdir(path.dirname(absFile), { recursive: true });
  await fs.writeFile(absFile, turtle, 'utf8');

  await git.add(relFile);
  const commit = await git.commit(message || `Concept edit ${safeName}`, [relFile], {
    '--author': `${cfg.authorName} <${cfg.authorEmail}>`,
  });

  let pushed = false;
  if (cfg.push) {
    if (cfg.remoteUrl && cfg.token) {
      await git.remote(['set-url', cfg.remote, authedUrl(cfg.remoteUrl, cfg.token)]);
    }
    await git.push(cfg.remote, cfg.branch, { '--set-upstream': null });
    pushed = true;
  }

  return { commit: commit.commit, branch: cfg.branch, file: relFile, pushed };
}

export const gitConfig = cfg;

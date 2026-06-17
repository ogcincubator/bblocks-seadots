# syntax=docker/dockerfile:1

# --- Stage 1: build the Vite SPA ----------------------------------------------
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci || npm install
COPY . .
# Build-time SPARQL/graph overrides can be baked in via --build-arg.
ARG VITE_SPARQL_QUERY
ARG VITE_SPARQL_UPDATE
ARG VITE_GRAPH
RUN npm run build

# --- Stage 2: runtime (static SPA + git API) ----------------------------------
FROM node:22-alpine AS runtime
# git is required by the commit/push endpoint.
RUN apk add --no-cache git openssh-client
WORKDIR /app
ENV NODE_ENV=production
# Install production deps only (express, simple-git).
COPY package.json package-lock.json* ./
RUN npm ci --omit=dev || npm install --omit=dev
COPY server ./server
COPY --from=build /app/dist ./dist

# Where the repo to commit into will live inside the container. It is cloned on
# first commit from GIT_REMOTE_URL using GIT_TOKEN (see server/git.mjs).
ENV REPO_DIR=/repo \
    PORT=8080 \
    GIT_BRANCH=concept-edits \
    EDITS_PATH=_sources/oim-variables/edits
RUN mkdir -p /repo && chown -R node:node /repo /app

USER node
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=4s --start-period=10s \
  CMD wget -qO- http://localhost:8080/api/health || exit 1
CMD ["node", "server/index.mjs"]

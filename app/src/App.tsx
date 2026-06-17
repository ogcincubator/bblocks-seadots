import { useEffect } from 'react';
import { Link, NavLink, Outlet } from 'react-router-dom';
import { useStore } from './store/useStore';
import ChangesPanel from './components/ChangesPanel';

export default function App() {
  const loadCatalog = useStore((s) => s.loadCatalog);
  const loading = useStore((s) => s.loading);
  const loadError = useStore((s) => s.loadError);

  useEffect(() => {
    void loadCatalog();
  }, [loadCatalog]);

  return (
    <div className="app">
      <header className="topbar">
        <Link to="/" className="brand">
          🌊 SeaDOTs Concept Editor
        </Link>
        <nav>
          <NavLink to="/" end>
            Browse
          </NavLink>
          <NavLink to="/concept/new">+ New concept</NavLink>
        </nav>
        <div className="topbar-status">
          {loading && <span className="muted">Loading vocabulary…</span>}
          {loadError && <span className="error">⚠ {loadError}</span>}
        </div>
      </header>
      <main className="content">
        <Outlet />
      </main>
      <ChangesPanel />
    </div>
  );
}

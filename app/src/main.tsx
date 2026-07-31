import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App';
import BrowserPage from './pages/BrowserPage';
import EditorPage from './pages/EditorPage';
import ConceptSchemePage from './pages/ConceptSchemePage';
import './styles.css';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      { index: true, element: <BrowserPage /> },
      { path: 'concept/new', element: <EditorPage /> },
      { path: 'concept/:iri', element: <EditorPage /> },
      { path: 'conceptScheme/:iri', element: <ConceptSchemePage /> },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);

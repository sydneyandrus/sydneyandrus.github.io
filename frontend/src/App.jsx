import { QueryClient, QueryClientProvider } from 'react-query';
import { Link, BrowserRouter, Navigate, Routes, Route } from 'react-router-dom';

import NavBar from "./components/NavBar";
import Library from "./components/Library";
import About from "./components/About";
import Diary from "./components/Diary";
import HomePage from "./components/HomePage";

const queryClient = new QueryClient();

function NotFound() {
  return <h1>404: not found</h1>;
}

function ErrorPage() {
  return (
    <>
      <h1>an error has occurred</h1>
      <p>contact site admin for support</p>
    </>
  );
}

function AboutPage() {
  return (
    <div>
      <NavBar/>
      <About/>
    </div>
  )
}

function DiaryPage() {
  return (
    <div>
      <NavBar/>
      <Diary/>
    </div>
  )
}

function LibraryPage() {
  return (
    <div>
      <NavBar/>
      <Library/>
    </div>
  )
}

function App() {
  const className = "h-dvh bg-amber-50 flex flex-col mx-auto max-w-3xl"

  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <div>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/diary" element={<DiaryPage />}>
              <Route path="/diary/:postId" element={<DiaryPage />} />
            </Route>
            <Route path="/library" element={<LibraryPage />}>
              <Route path="/library/:group" element={<LibraryPage />} />
              <Route path="/library/:group/:id" element={<LibraryPage />} />
            </Route>
            <Route path="/about" element={<AboutPage />} />
            <Route path="/error" element={<ErrorPage />} />
            <Route path="/error/404" element={<NotFound />} />
            <Route path="*" element={<Navigate to="/error/404" />} />
          </Routes>
        </div>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App
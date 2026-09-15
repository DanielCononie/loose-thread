import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import OpenCase from "./components/OpenCase";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/open-case" element={<OpenCase />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import AllTeams from './components/AllTeams';
import HomePage from './pages/HomePage';

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/teams" element={<AllTeams />} />
        </Routes>
      </Router>
  );
}

export default App;

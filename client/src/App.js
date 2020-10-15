import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './App.css';

//Components
import Login from "./components/authentication/Login";
import Navbar from "./components/layout/Navbar";
import Landing from "./components/layout/Landing";
import Submit from "./components/submissions/Submit";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Route exact path="/" component={Landing} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/submission" component={Submit} />
    </div>
    </Router>
    
  );
}

export default App;

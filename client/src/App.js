import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "./App.css";

import { Provider } from "react-redux";
import store from "./store";

//Components
import Login from "./components/authentication/Login";
import Navbar from "./components/layout/Navbar";
import Landing from "./components/layout/Landing";
import Submit from "./components/submissions/Submit";
import PrivateRoute from "./components/private-route/PrivateRoute";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="App">
          <Navbar />
          <Route exact path="/" component={Landing} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/submission" component={Submit} />

          {/* Uncomment this section and remove previous "submission" when Auth
         is completed */}
          {/* <Switch>
          <PrivateRoute exact path="/submission" component={Submit} />
        </Switch> */}
        </div>
      </Router>
    </Provider>
  );
}

export default App;

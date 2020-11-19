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
import setAuthToken from "./utils/setAuthToken";
import { logoutUser, setCurrentUser } from "./actions/authAction";
import jwtDecode from "jwt-decode";

if (localStorage.jwtToken) {
  const token = localStorage.jwtToken;
  setAuthToken(token);

  const decoded = jwtDecode(token);

  store.dispatch(setCurrentUser(decoded));

  const currentTime = Date.now() / 100000;
  if (decoded.exp < currentTime) {
    console.log(currentTime);
    console.log(decoded.exp);
    store.dispatch(logoutUser());

    window.location.href = "./login";
  }
}
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

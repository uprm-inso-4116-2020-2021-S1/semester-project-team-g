import axios from "axios";
import setAuthToken from "../utils/setAuthToken";
import jwt from "jwt-decode";

import { GET_ERRORS, SET_CURRENT_USER, USER_LOADING } from "./types";

//Login
export const loginUser = (userData, history) => (dispatch) => {
  axios
    .post("http://localhost:5000/operator-login", userData, { headers : {"Access-Control-Allow-Origin": "*"}}) //MUST CHANGE TO ACTUAL ENDPOINT ESTABLISHED IN BACKEND
    .then((res) => {
        const { token } = res.data;
        localStorage.setItem("jwtToken", token);

        setAuthToken(token);

        const decoded = jwt(token);

        dispatch(setCurrentUser(decoded));
    })
    .catch(err =>
      dispatch({
        type: GET_ERRORS,
        payload: err.response.data
      }));
};

//Set logged in user
export const setCurrentUser = (decoded) => {
  return {
    type: SET_CURRENT_USER,
    payload: decoded,
  };
};

//User load
export const setUserLoading = () => {
  return {
    type: USER_LOADING,
  };
};

//Log out user
export const logoutUser = () => (dispatch) => {
  localStorage.removeItem("jwtToken");
  setAuthToken(false);
  dispatch(setCurrentUser({}));
};

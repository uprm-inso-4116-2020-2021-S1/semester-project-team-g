/*
Combine all of our reducers into a single root 
reducer for the store
*/

import { combineReducers } from "redux";
import authReducers from "./authReducer";
import submitReducers from "./submitReducer";
import errorReducers from "./errorReducer";

export default combineReducers({
    auth: authReducers,
    submit: submitReducers,
    error: errorReducers
})
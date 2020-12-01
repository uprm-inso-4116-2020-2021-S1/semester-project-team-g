import axios from "axios";

import { SUBMIT_INFO, GET_ERRORS, GET_INFO, INFO_LOADING } from "./types";

export const submitInfo = (patientInfo, history) => async (dispatch) => {
  let response = await axios
    .post("http://localhost:5000/input-form", patientInfo)
    .catch((err) =>
      dispatch({
        type: GET_ERRORS,
        payload: err.response.data,
      })
    );
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    dispatch({
      type: SUBMIT_INFO,
      payload: data,
    });
    return true;
  }
};

export const updateInfo = (updatedInfo) => async (dispatch) => {
  let response = await axios
    .put("http://localhost:5000/update-form", updatedInfo)
    .catch((err) =>
      dispatch({
        type: GET_ERRORS,
        payload: err.response.data,
      })
    );
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    dispatch({
      type: SUBMIT_INFO,
      payload: data,
    });
    return true;
  }
};

export const addTest = (testData) => async (dispatch) => {
  let response = await axios
    .post("http://localhost:5000/add-test", testData)
    .catch((err) =>
      dispatch({
        type: GET_ERRORS,
        payload: err.response.data,
      })
    );
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    dispatch({
      type: SUBMIT_INFO,
      payload: data,
    });
    return true;
  }
};

export const getInfo = (patientSSN) => (dispatch) => {
  dispatch(setPatientLoading());
  axios
    .get(`/${patientSSN}`)
    .then((patientInfo) =>
      dispatch({
        type: GET_INFO,
        payload: patientInfo.data,
      })
    )
    .catch((err) =>
      dispatch({
        type: GET_ERRORS,
        payload: err.response.data,
      })
    );
};

export const setPatientLoading = () => {
  return {
    type: INFO_LOADING,
  };
};

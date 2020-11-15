import axios from "axios";

import { SUBMIT_INFO, GET_ERRORS, GET_INFO, INFO_LOADING } from "./types";

export const submitInfo = (patientInfo) => (disptach) => {
  axios
    .post("/", patientInfo) //BACKEND ENDPOINT
    .then((res) => {
      disptach({
        type: SUBMIT_INFO,
        payload: res.data,
      });
      //might push user to another page here.
    })
    .catch((err) =>
      disptach({
        type: GET_ERRORS,
        payload: err.response.data,
      })
    );
};

export const getInfo = (patientSSN) => (disptach) => {
  disptach(setPatientLoading());
  axios
    .get(`/${patientSSN}`)
    .then((patientInfo) =>
      disptach({
        type: GET_INFO,
        payload: patientInfo.data,
      })
    )
    .catch((err) =>
      disptach({
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

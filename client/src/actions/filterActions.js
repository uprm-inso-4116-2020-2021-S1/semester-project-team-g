import axios from "axios";
import { GET_ERRORS } from "./types";

export const globalFilter = (filterData) => async (dispatch) => {
  let pType = filterData.patientType === "infected" ? "infected" : "recovered";
  let response = await axios
    .get(`http://localhost:5000/${pType}/results-global`)
    .catch((err) => dispatch({ type: GET_ERRORS, payload: err.response.data }));
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    return data;
  } else {
    return {};
  }
};

export const ageFilter = (filterData) => async (dispatch) => {
  let pType = filterData.patientType === "infected" ? "infected" : "recovered";
  let response = await axios
    .get(
      `http://localhost:5000/${pType}/results-age/${filterData.min_age}&${filterData.max_age}`
    )
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
    return data;
  } else {
    return {};
  }
};

export const municipalityFilter = (filterData) => async (dispatch) => {
  let pType = filterData.patientType === "infected" ? "infected" : "recovered";
  let illness = filterData.illness ? `/${filterData.illness}` : "";
  let response = await axios
    .get(
      `http://localhost:5000/${pType}/results-municipality/${filterData.municipality}${illness}`
    )
    .catch((err) => dispatch({ type: GET_ERRORS, payload: err.response.data }));
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    return data;
  } else {
    return {};
  }
};

export const sexFilter = (filterData) => async (dispatch) => {
  let pType = filterData.patientType === "infected" ? "infected" : "recovered";
  let illness = filterData.illness ? `/${filterData.illness}` : "";
  let response = await axios
    .get(
      `http://localhost:5000/${pType}/results-sex/${filterData.sex}${illness}`
    )
    .catch((err) => dispatch({ type: GET_ERRORS, payload: err.response.data }));
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    return data;
  } else {
    return {};
  }
};

export const monthFilter = (filterData) => async (dispatch) => {
  let pType = filterData.patientType === "infected" ? "infected" : "recovered";
  let illness = filterData.illness ? `/${filterData.illness}` : "";
  let response = await axios
    .get(
      `http://localhost:5000/${pType}/results-month/${filterData.month}${illness}`
    )
    .catch((err) => dispatch({ type: GET_ERRORS, payload: err.response.data }));
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {},
    });
    return data;
  } else {
    return {};
  }
};

export const yearFilter = (filterData) => async (dispatch) => {
  let pType = filterData.patientType === "infected" ? "infected" : "recovered";
  let illness = filterData.illness ? `/${filterData.illness}` : "";
  let response = await axios.get(
    `http://localhost:5000/${pType}/results-year/${filterData.year}${illness}`
  )
  .catch((err) => dispatch({ type: GET_ERRORS, payload: err.response.data }));
  let data = await response.data;
  if (data) {
    dispatch({
      type: GET_ERRORS,
      payload: {}
    });
    return data;
  } else {
    return {}
  }
};

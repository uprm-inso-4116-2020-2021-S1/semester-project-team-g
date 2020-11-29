import axios from "axios";
import { GET_ERRORS } from "./types";

export const globalFilter = () => async dispatch => {
  let response = await axios.get("http://localhost:5000/results-global");
  let data = await response.data;
  return data;
};

export const ageFilter = (filterData) => async (dispatch) => {
    let response = await axios
        .get(`http://localhost:5000/results-age/${filterData.min_age}&${filterData.max_age}`)
        .catch((err) =>
            dispatch({
                type: GET_ERRORS,
                payload: err.response.data
            })
        )
    let data = await response.data;
    if (data) {
        dispatch({
            type: GET_ERRORS,
            payload: {}
        })
        return data;
    }
    else {
        return {}
    }
}

  export const municipalityFilter = (filterData) => async dispatch => {
    let response = await axios.get(`http://localhost:5000/results-municipality/${filterData.municipality}`);
    let data = await response.data;
    return data;
  };

  export const sexFilter = (filterData) => async dispatch => {
    let response = await axios.get(`http://localhost:5000/results-sex/${filterData.sex}`);
    let data = await response.data;
    return data;
  };

  export const monthFilter = (filterData) => async dispatch => {
    let response = await axios.get(`http://localhost:5000/results-month/${filterData.month}`);
    let data = await response.data;
    return data;
  };

  export const yearFilter = (filterData) => async dispatch => {
    let response = await axios.get(`http://localhost:5000/results-year/${filterData.year}`);
    let data = await response.data;
    return data;
  };
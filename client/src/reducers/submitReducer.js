import { SUBMIT_INFO, GET_INFO} from "../actions/types";

const initialState = {
    patientInfo: Object,
    patientLoading: false
};

export default function(state = initialState, action) {
    switch(action.type) {
        case SUBMIT_INFO:
            return {
                ...state,
                patientInfo: action.payload
            };
        case GET_INFO:
            return {
                ...state,
                patientInfo: action.payload,
                patientLoading: false
            };
        case INFO_LOADING:
            return {
                ...state,
                patientLoading: true
            }
        default:
            return state;
    }
}
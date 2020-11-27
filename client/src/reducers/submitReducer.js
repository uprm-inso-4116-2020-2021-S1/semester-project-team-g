import { SUBMIT_INFO, GET_INFO, INFO_LOADING} from "../actions/types";

const initialState = {
    patientInfo: [],
    patientLoading: false
};

export default function(state = initialState, action) {
    switch(action.type) {
        case SUBMIT_INFO:
            return {
                ...state,
                patientInfo: [action.payload, ...state.patientInfo]
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
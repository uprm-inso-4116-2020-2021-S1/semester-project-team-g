import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { connect } from "react-redux";
import { submitInfo, updateInfo, addTest } from "../../actions/submitAction";
import PropTypes from "prop-types";

import "./Submit.css";

class Submit extends Component {
  constructor() {
    super();
    this.state = {
      firstname: "",
      lastname: "",
      address: "",
      dateOfBirth: "",
      phone: "",
      email: "",
      sex: "male",
      ssn: "",
      ishp: "deceased",

      //Test Data
      illness: "",
      is_positive: "negative",
      institution_name: "",

      //Errors
      error: {},

      //State
      submission_option: "", //Add new, update info, update test

      //For side panel
      status: [],
    };
    this.initialState = this.state;
    delete this.initialState["error"];
  }

  resetState() {
    this.setState(this.initialState);
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    if (nextProps.error !== prevState.error) {
      return { error: nextProps.error };
    } else return null;
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.error !== this.props.error) {
      //Perform some operation here
      this.setState({ error: prevProps.error });
    }
  }

  componentDidMount() {
    if (!this.props.auth.isAuthenticated) {
      this.props.history.push("/login");
    }
  }

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  disableInput = () => {
    if (!this.state.submission_option) {
      return false;
    } else {
      return true;
    }
  };

  onSubmit = async (e) => {
    e.preventDefault();
    const patientData = {
      firstname: this.state.firstname,
      lastname: this.state.lastname,
      address: this.state.address,
      date_of_birth: this.state.dateOfBirth,
      phone: this.state.phone,
      email: this.state.email,
      sex: this.state.sex === "male" ? "m" : "f",
      ssn: this.state.ssn,
      ishp: this.state.ishp === "alive" ? true : false,
      illness: this.state.illness,
      is_positive: this.state.is_positive === "positive" ? true : false,
      institution_name: this.state.institution_name,
      oid: this.props.auth.user.oid,
    };
    let res = await this.props.submitInfo(patientData, this.props.history);
    if (res) {
      this.resetState();
    }
  };

  onUpdate = async (e) => {
    e.preventDefault();
    const updatedData = {
      firstname: this.state.firstname,
      lastname: this.state.lastname,
      address: this.state.address,
      date_of_birth: this.state.dateOfBirth,
      phone: this.state.phone,
      email: this.state.email,
      sex: this.state.sex === "male" ? "m" : "f",
      ssn: this.state.ssn,
      ishp: this.state.ishp === "alive" ? true : false,
      oid: this.props.auth.user.oid,
    };
    let res = await this.props.updateInfo(updatedData);
    if (res) {
      this.resetState();
    }
  };

  onTest = async (e) => {
    e.preventDefault();
    const testData = {
      ssn: this.state.ssn,
      illness: this.state.illness,
      is_positive: this.state.is_positive === "positive" ? true : false,
      institution_name: this.state.institution_name,
      oid: this.props.auth.user.oid
    };
    let res = await this.props.addTest(testData);
    if (res) {
      this.resetState();
    }
  }

  render() {
    let ssn = this.state.ssn;
    let content;
    let illnessData;
    let ispositiveData;
    let locationData;
    let sidePanel;
    const { error } = this.state;
    if (
      Number(ssn.length) === 9 &&
      Number.isFinite(parseInt(ssn)) &&
      (this.state.submission_option === "add_patient_case" ||
        this.state.submission_option === "add_patient_test")
    ) {
      //When we get a ssn number
      //We'll check if it exists or not.
      //If it does we'll autofill the entries
      if (
        this.state.ishp === "alive" &&
        (this.state.submission_option === "add_patient_case" ||
          this.state.submission_option === "add_patient_test")
      ) {
        illnessData = (
          <Form.Group controlId="illness">
            <Form.Label>Illness</Form.Label>
            <Form.Control
              required
              onChange={this.onChange}
              value={this.state.illness}
              type="text"
              isInvalid={error.illness}
              placeholder="Enter Illness"
            />
            <Form.Control.Feedback type="invalid">
              {error.illness}
            </Form.Control.Feedback>
          </Form.Group>
        );
        ispositiveData = (
          <Form.Group controlId="is_positive">
            <Form.Label>Illness Status</Form.Label>
            <Form.Control
              required
              onChange={this.onChange}
              value={this.state.is_positive}
              as="select"
              custom
              isInvalid={error.is_positive}
              placeholder="Select status"
            >
              <option value="negative">Negative</option>
              <option value="positive">Positive</option>
            </Form.Control>
            <Form.Control.Feedback type="invalid">
              {error.is_positive}
            </Form.Control.Feedback>
          </Form.Group>
        );
        locationData = (
          <Form.Group controlId="institution_name">
            <Form.Label>Institution Name</Form.Label>
            <Form.Control
              required
              onChange={this.onChange}
              value={this.state.institution_name}
              type="text"
              isInvalid={error.institution}
              placeholder="Enter Institution Name"
            />
            <Form.Control.Feedback type="invalid">
              {error.institution}
            </Form.Control.Feedback>
          </Form.Group>
        );
      }
      if (this.state.submission_option === "add_patient_case") {
        content = (
          <Container className="form">
            <Row className="form">
              <div style={{ paddingTop: "20px" }}>
                <b>Please provide the patient's information</b>
              </div>
              <Col className="form">
                <Form ref="form" onSubmit={this.onSubmit}>
                  <Form.Group controlId="firstname">
                    <Form.Label>Firstname</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.firstname}
                      type="text"
                      isInvalid={error.first_name}
                      placeholder="Enter Firstname"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.first_name}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="lastname">
                    <Form.Label>Lastname</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.lastname}
                      type="text"
                      isInvalid={error.last_name}
                      placeholder="Enter Lastname"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.last_name}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="address">
                    <Form.Label>Address</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.address}
                      type="text"
                      isInvalid={error.address}
                      placeholder="Enter Address"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.address}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="dateOfBirth">
                    <Form.Label>Date Of Birth</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.dateOfBirth}
                      type="text"
                      isInvalid={error.date_of_birth}
                      placeholder="Enter Date in DD/MM/YYYY"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.date_of_birth}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="phone">
                    <Form.Label>Phone Number</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.phone}
                      type="text"
                      isInvalid={error.phone}
                      placeholder="Enter Phone Number"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.phone}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="email">
                    <Form.Label>Email Address</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.email}
                      type="email"
                      isInvalid={error.email}
                      placeholder="Enter Email Address"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.email}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="sex">
                    <Form.Label>Sex</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.sex}
                      as="select"
                      custom
                      isInvalid={error.sex}
                      placeholder="Select sex"
                    >
                      <option value="male">Male</option>
                      <option value="female">Female</option>
                    </Form.Control>
                    <Form.Control.Feedback type="invalid">
                      {error.sex}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="ssn">
                    <Form.Label>SSN</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.ssn}
                      type="text"
                      isInvalid={error.ssn}
                      placeholder="Enter Patient Social Security Number"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.ssn}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="ishp">
                    <Form.Label>Patient Status</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.ishp}
                      as="select"
                      custom
                      isInvalid={error.ishp}
                      placeholder="Select status"
                    >
                      <option value="alive">Alive</option>
                      <option value="deceased">Deceased</option>
                    </Form.Control>
                    <Form.Control.Feedback type="invalid">
                      {error.ishp}
                    </Form.Control.Feedback>
                  </Form.Group>
                  {illnessData}
                  {ispositiveData}
                  {locationData}
                  <Button variant="primary" type="submit" block>
                    Submit
                  </Button>
                </Form>
              </Col>
            </Row>
          </Container>
        );
      } else {
        content = (
          <Container className="form">
            <Row className="form">
              <div style={{ paddingTop: "20px" }}>
                <b>Please provide the patient's information</b>
              </div>
              <Col className="form">
                <Form ref="form" onSubmit={this.onTest}>
                  <Form.Group controlId="ssn">
                    <Form.Label>SSN</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.ssn}
                      type="text"
                      isInvalid={error.ssn}
                      placeholder="Enter Patient Social Security Number"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.ssn}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="illness">
                    <Form.Label>Illness</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.illness}
                      type="text"
                      isInvalid={error.illness}
                      placeholder="Enter Illness"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.illness}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="is_positive">
                    <Form.Label>Illness Status</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.is_positive}
                      as="select"
                      custom
                      isInvalid={error.is_positive}
                      placeholder="Select status"
                    >
                      <option value="negative">Negative</option>
                      <option value="positive">Positive</option>
                    </Form.Control>
                    <Form.Control.Feedback type="invalid">
                      {error.is_positive}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group controlId="institution_name">
                    <Form.Label>Institution Name</Form.Label>
                    <Form.Control
                      required
                      onChange={this.onChange}
                      value={this.state.institution_name}
                      type="text"
                      isInvalid={error.institution}
                      placeholder="Enter Institution Name"
                    />
                    <Form.Control.Feedback type="invalid">
                      {error.institution}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Button variant="primary" type="submit" block>
                    Submit
                  </Button>
                </Form>
              </Col>
            </Row>
          </Container>
        );
      }
    } else if (
      Number(ssn.length) === 9 &&
      Number.isFinite(parseInt(ssn)) &&
      this.state.submission_option === "update_patient_info"
    ) {
      content = (
        <Container className="form">
          <Row className="form">
            <div style={{ paddingTop: "20px" }}>
              <b>Please provide the patient's information</b>
            </div>
            <Col className="form">
              <Form ref="form" onSubmit={this.onUpdate}>
                <Form.Group controlId="firstname">
                  <Form.Label>Firstname</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.firstname}
                    type="text"
                    isInvalid={error.first_name}
                    placeholder="Enter Firstname"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.first_name}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="lastname">
                  <Form.Label>Lastname</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.lastname}
                    type="text"
                    isInvalid={error.last_name}
                    placeholder="Enter Lastname"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.last_name}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="address">
                  <Form.Label>Address</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.address}
                    type="text"
                    isInvalid={error.address}
                    placeholder="Enter Address"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.address}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="dateOfBirth">
                  <Form.Label>Date Of Birth</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.dateOfBirth}
                    type="text"
                    isInvalid={error.date_of_birth}
                    placeholder="Enter Date in DD/MM/YYYY"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.date_of_birth}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="phone">
                  <Form.Label>Phone Number</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.phone}
                    type="text"
                    isInvalid={error.phone}
                    placeholder="Enter Phone Number"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.phone}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="email">
                  <Form.Label>Email Address</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.email}
                    type="email"
                    isInvalid={error.email}
                    placeholder="Enter Email Address"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.email}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="sex">
                  <Form.Label>Sex</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.sex}
                    as="select"
                    custom
                    isInvalid={error.sex}
                    placeholder="Select sex"
                  >
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                  </Form.Control>
                  <Form.Control.Feedback type="invalid">
                    {error.sex}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="ssn">
                  <Form.Label>SSN</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.ssn}
                    type="text"
                    isInvalid={error.ssn}
                    placeholder="Enter Patient Social Security Number"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.ssn}
                  </Form.Control.Feedback>
                </Form.Group>
                <Form.Group controlId="ishp">
                  <Form.Label>Patient Status</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.ishp}
                    as="select"
                    custom
                    isInvalid={error.ishp}
                    placeholder="Select status"
                  >
                    <option value="alive">Alive</option>
                    <option value="deceased">Deceased</option>
                  </Form.Control>
                  <Form.Control.Feedback type="invalid">
                    {error.ishp}
                  </Form.Control.Feedback>
                </Form.Group>
                <Button variant="primary" type="submit" block>
                  Submit
                </Button>
              </Form>
            </Col>
          </Row>
        </Container>
      );
    } else {
      content = (
        <Container className="form">
          <Row className="form">
            <div style={{ paddingTop: "20px" }}>
              <b>Please provide the patient's information</b>
            </div>
            <Col className="form">
              <Form onSubmit={this.onUpdate}>
                <Form.Group controlId="ssn">
                  <Form.Label>SSN</Form.Label>
                  <Form.Control
                    required
                    disabled={!this.disableInput()}
                    onChange={this.onChange}
                    value={this.state.ssn}
                    type="text"
                    placeholder="Enter Patient Social Security Number"
                  />
                </Form.Group>
                <fieldset>
                  <Form.Group controlId="submission_option">
                    <Form.Check
                      onChange={(e) => {
                        this.setState({
                          submission_option: "add_patient_case",
                        });
                      }}
                      name="radios"
                      value={this.state.submission_option}
                      type="radio"
                      label="Add new Patient case."
                    />
                    <Form.Check
                      onChange={(e) => {
                        this.setState({
                          submission_option: "update_patient_info",
                        });
                      }}
                      name="radios"
                      value={this.state.submission_option}
                      type="radio"
                      label="Update Patient info."
                    />
                    <Form.Check
                      onChange={(e) => {
                        this.setState({
                          submission_option: "add_patient_test",
                        });
                      }}
                      name="radios"
                      value={this.state.submission_option}
                      type="radio"
                      label="Add new test to existing Patient."
                    />
                  </Form.Group>
                </fieldset>
              </Form>
            </Col>
          </Row>
        </Container>
      );
    }
    let statusMap;
    statusMap = this.props.submit.patientInfo.map((stat) => (
      <div className="side-panel-entry" key={stat.message}>
        <a>{stat.message}</a>
      </div>
    ));
    sidePanel = (
      <div className="side-panel-container">
        <div className="side-panel">
          <div className="side-panel-title">
            <h4>Status Panel</h4>
          </div>
          <div className="side-panel-content">{statusMap}</div>
        </div>
      </div>
    );

    return (
      <div className="content">
        {content}
        {sidePanel}
      </div>
    );
  }
}

Submit.propTypes = {
  submitInfo: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired,
  error: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  auth: state.auth,
  error: state.error,
  submit: state.submit,
});

export default connect(mapStateToProps, { submitInfo, updateInfo, addTest })(Submit);

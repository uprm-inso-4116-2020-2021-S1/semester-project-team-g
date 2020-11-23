import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { connect } from "react-redux";
import { submitInfo } from "../../actions/submitAction";

class Submit extends Component {
  constructor() {
    super();
    this.state = {
      firstname: "",
      lastname: "",
      address: "",
      dateOfBirth: "",
      phone: "",
      sex: "male",
      ssn: "",
      ishp: "alive",

      //Test Data
      illness: "",
      is_positive: "negative",
      institution_name: "",
      timestamp: "",
      error: {}
    };
  }

  componentDidMount() {
    if (!this.props.auth.isAuthenticated) {
      this.props.history.push("/login");
    }
  }

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();
    const patientData = {
      firstname: this.state.firstname,
      lastname: this.state.lastname,
      address: this.state.address,
      date_of_birth: this.state.dateOfBirth,
      phone: this.state.phone,
      sex: this.state.sex,
      ssn: this.state.ssn,
      ishp: this.state.ishp === "alive" ? true : false,
      illness: this.state.illness,
      is_positive: this.state.is_positive === "positive" ? true : false,
      institution_name: this.state.institution_name,
      timestamp: this.state.timestamp
    }
    this.props.submitInfo(patientData, this.props.history);
  };

  render() {
    console.log(this.state);
    let ssn = this.state.ssn;
    let content;
    let illnessData;
    let ispositiveData;
    let locationData;
    let timestampData;
    const { error } = this.state;
    if (Number(ssn.length) === 9 && Number.isFinite(parseInt(ssn))) {
      //When we get a ssn number
      //We'll check if it exists or not.
      //If it does we'll autofill the entries
      if(this.state.ishp === "alive") {
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
          </Form.Group>)
        ispositiveData= ( 
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
          </Form.Group>)
        locationData = (
          <Form.Group controlId="institution_name">
            <Form.Label>Location</Form.Label>
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
          </Form.Group>)
        timestampData = (
            <Form.Group controlId="timestamp">
              <Form.Label>Timestamp</Form.Label>
              <Form.Control
                required
                onChange={this.onChange}
                value={this.state.timestamp}
                type="text"
                placeholder="Enter Date"
              />
            </Form.Group>)
      }
      content = (
        <Container style={{ width: "400px" }}>
          <Row
            className="form justify-content-center"
            style={{
              marginTop: "40px",
              backgroundColor: "white",
              borderRadius: "5px",
            }}
          >
            <div style={{ paddingTop: "20px" }}>
              <b>Please provide the patient's information</b>
            </div>
            <Col style={{ padding: "20px" }}>
              <Form onSubmit={this.onSubmit}>
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
                    placeholder="Enter Lastname"
                  />
                </Form.Group>
                <Form.Group controlId="address">
                  <Form.Label>Address</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.address}
                    type="text"
                    isInvalid={error.last_name}
                    placeholder="Enter Address"
                  />
                  <Form.Control.Feedback type="invalid">
                    {error.last_name}
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
                    placeholder="Enter Age"
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
                {timestampData}
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
        <Container style={{ width: "400px" }}>
          <Row
            className="form justify-content-center"
            style={{
              marginTop: "40px",
              backgroundColor: "white",
              borderRadius: "5px",
            }}
          >
            <div style={{ paddingTop: "20px" }}>
              <b>Please provide the patient's information</b>
            </div>
            <Col style={{ padding: "20px" }}>
              <Form onSubmit={this.onSubmit}>
                <Form.Group controlId="ssn">
                  <Form.Label>SSN</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.ssn}
                    type="text"
                    placeholder="Enter Patient Social Security Number"
                  />
                </Form.Group>
              </Form>
              <span>OR</span>
              <Button variant="primary" type="file" block>
                Upload csv file
              </Button>
            </Col>
          </Row>
        </Container>
      );
    }

    return (<div>
          {content}
          </div>
    )
  }
}

const mapStateToProps = state => ({
  auth: state.auth,
  error: state.error,
  submit: state.submit
})

export default connect(mapStateToProps, { submitInfo })(Submit);

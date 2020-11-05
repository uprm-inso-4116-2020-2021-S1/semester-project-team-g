import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class Submit extends Component {
  constructor() {
    super();
    this.state = {
      firstname: "",
      lastname: "",
      address: "",
      age: "",
      sex: "",
      location: "",
      ssn: "",
    };
  }

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();
  };

  render() {
    let ssn = this.state.ssn; //Testing
    let content;
    if (Number(ssn.length) === 4) {
      //When we get a ssn number
      //We'll check if it exists or not.
      //If it does we'll autofill the entries
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
                    placeholder="Enter Firstname"
                  />
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
                    placeholder="Enter Address"
                  />
                </Form.Group>
                <Form.Group controlId="age">
                  <Form.Label>Age</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.age}
                    type="text"
                    placeholder="Enter Age"
                  />
                </Form.Group>
                <Form.Group controlId="sex">
                  <Form.Label>Sex</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.sex}
                    as="select"
                    custom
                    placeholder="Select sex"
                  >
                    <option value="1">Male</option>
                    <option value="3">Female</option>
                  </Form.Control>
                </Form.Group>
                <Form.Group controlId="location">
                  <Form.Label>Location</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.location}
                    type="text"
                    placeholder="Enter Institute Location"
                  />
                </Form.Group>
                <Form.Group controlId="ssn">
                  <Form.Label>SSN</Form.Label>
                  <Form.Control
                    required
                    onChange={this.onChange}
                    value={this.state.ssn}
                    type="text"
                    placeholder="Enter last 4-digits of SSN"
                  />
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
                    placeholder="Enter last 4-digits of SSN"
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

    return <div>{content}</div>;
  }
}

export default Submit;

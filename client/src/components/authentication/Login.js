import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Image from "react-bootstrap/Image";
import logo from "./logo-removebg-preview.png";

class Login extends Component {
  constructor() {
    super();
    this.state = {
      email: "",
      password: "",
    };
  }

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();
    this.props.history.push('/submission')
    //Redirect to dashboard
  };

  render() {
    return (
      <Container style={{ width: "400px" }}>
        <Row className="text-center" style={{marginTop: "20px"}}>
          <Col>
          <Image src={logo} width="200" height="200"/>
          </Col>
        </Row>
        <Row
          className="form justify-content-center"
          style={{
            marginTop: "40px",
            backgroundColor: "white",
            borderRadius: "5px",
          }}
        >
          <Col style={{ padding: "20px" }}>
            <Form onSubmit={this.onSubmit}>
              <Form.Group controlId="email">
                <Form.Label>Email</Form.Label>
                <Form.Control
                  required
                  onChange={this.onChange}
                  value={this.state.email}
                  type="email"
                  placeholder="Enter Email"
                />
              </Form.Group>
              <Form.Group controlId="password">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  required
                  onChange={this.onChange}
                  value={this.state.password}
                  type="password"
                  placeholder="Enter Password"
                />
              </Form.Group>
              <Button variant="primary" type="submit" block>
                Log in
              </Button>
            </Form>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Login;

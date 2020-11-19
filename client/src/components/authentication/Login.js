import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Image from "react-bootstrap/Image";
import logo from "./logo-removebg-preview.png";

import PropTypes from "prop-types";
import { withRouter } from "react-router-dom";
import { connect } from "react-redux";
import { loginUser } from "../../actions/authAction";

class Login extends Component {
  constructor() {
    super();
    this.state = {
      username: "",
      password: "",
      error: {}
    };
  }

  componentDidMount() {
    // If logged in and user navigates to Login page, should redirect them to dashboard
    if (this.props.auth.isAuthenticated) {
      this.props.history.push("/submission");
    }
  };

  UNSAFE_componentWillReceiveProps(nextProps) {
    if (nextProps.auth.isAuthenticated) {
      this.props.history.push("/submission");
    }

    if (nextProps.error) {
      this.setState({
        error: nextProps.error,
      });
    }
  };

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();
    const userData = {
      username: this.state.username,
      password: this.state.password
    };
    this.props.loginUser(userData, this.props.history);
  };

  render() {
    const { error } = this.state;
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
              <Form.Group controlId="username">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  required
                  onChange={this.onChange}
                  value={this.state.username}
                  isInvalid={error.message}
                  type="text"
                  placeholder="Enter Username"
                />
                <Form.Control.Feedback type="invalid">
                  {error.message}
                </Form.Control.Feedback>
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

Login.propTypes = {
  loginUser: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired,
  error: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
  auth: state.auth,
  error: state.error
});

export default connect(mapStateToProps, { loginUser })(withRouter(Login));

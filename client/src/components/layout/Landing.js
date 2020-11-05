import React, { Component } from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Image from "react-bootstrap/Image";
import logo from "../authentication/logo-removebg-preview.png";

class Landing extends Component {
  render() {
    return (
      <Container
        fluid
        style={{
          display: "flex",
          justifyContent: "center",
          minHeight: "50vh",
          overflow: "hidden",
        }}
      >
        <Row style={{ width: "33.33%" }}>
          <Col style={{ textAlign: "center" }}>
            <p>About Us</p>
          </Col>
        </Row>
        <Row style={{ width: "33.33%" }}>
          <Col style={{ textAlign: "center", alignSelf: "flex-end" }}>
          <Image src={logo} width="200" height="200" />
            <div>
              <h2>Saving lives one at a time</h2>
            </div>
            <Button variant="primary" href="/login">
              Login
            </Button>
          </Col>
        </Row>
        <Row style={{ width: "33.33%" }}>
          <Col style={{ textAlign: "center" }}>
            <p>Contact Us</p>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Landing;

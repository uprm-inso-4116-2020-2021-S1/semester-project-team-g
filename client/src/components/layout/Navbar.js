import React, { Component } from "react";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";

class NavigationalBar extends Component {
  render() {
    return (
      <Navbar bg="dark" variant="dark">
        <Container className="justify-content-center">
          <Navbar.Brand href="/">Count The Homies</Navbar.Brand>
        </Container>
      </Navbar>
    );
  }
}

export default NavigationalBar;
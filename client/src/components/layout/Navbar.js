import React, { Component } from "react";
import Navbar from "react-bootstrap/Navbar";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import { connect } from "react-redux";
import { logoutUser } from "../../actions/authAction";

class NavigationalBar extends Component {

  onCLickLogout = e => {
    this.props.logoutUser();
  }

  render() {
    let logoutButton;
    if(this.props.auth.isAuthenticated) {
      logoutButton = (
        <Button style={{position: "absolute", marginLeft: "85%"}} onClick={this.onCLickLogout} href="/login">
          Logout
        </Button>
      )
    }
    return (
      <Navbar bg="dark" variant="dark">
        <Container className="justify-content-center">
          <Navbar.Brand href="/">Count The Homies</Navbar.Brand>
          {logoutButton}
        </Container>
      </Navbar>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
})

// export default NavigationalBar;
export default connect(mapStateToProps, { logoutUser })(NavigationalBar);
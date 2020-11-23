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
            <p style={{backgroundColor:"#007bff", padding: "12px", borderRadius: "8px", color:"white"}}>
              We are an organization that wishes to help the increasingly 
              difficult COVID-19 situation in Puerto Rico. Advances in the use of technology
              for the accounting and tracking of COVID cases have not been much. This has then resulted
              in a population that is tremendously worried about the worsening situation in Puerto Rico.
              That's why we propose the use of Count The Homies, a platform for authorized laboratories and
              institutions to use for the reporting and filing of COVID cases in Puerto Rico. In conjunction with
              the government of Puerto Rico and these institutions we hope to leviate the public's concern by providing accurate
              statistics on current COVID cases.
              <br/>
              <br/>
              We also have plans to expand our services to multiple other illnesses. This way we can provide
              the public with information regarding to already existing common illnesses, so that you and your family
              can have up-to-date information on the health status of Puerto Rico.
            </p>
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
            <p style={{backgroundColor:"#007bff", padding: "12px", borderRadius: "8px", color:"white"}}>
            If you wish to contact our headquarters. You can reach us at 1-800-###-#### for more information on
            Puerto Rico's COVID-19 situation, or if you need any technical support.
            </p>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Landing;

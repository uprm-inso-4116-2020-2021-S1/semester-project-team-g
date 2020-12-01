import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import { connect } from "react-redux";

import "./Statistics.css";

import {
  globalFilter,
  ageFilter,
  municipalityFilter,
  sexFilter,
  monthFilter,
  yearFilter,
} from "../../actions/filterActions";

class Statistics extends Component {
  constructor() {
    super();
    this.state = {
      patientType: "infected",
      option: "global",
      min_age: 0,
      max_age: 0,
      sex: "m",
      municipality: "",
      month: "01",
      year: "",
      illness: "",
      result: {},
      error: {},
    };
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

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  onSubmit = async (e) => {
    e.preventDefault();
    let filterData;
    let result;
    switch (this.state.option) {
      case "global":
        filterData = {
          patientType: this.state.patientType,
        };
        result = await this.props.globalFilter(filterData);
        this.setState({ result: result });
        break;
      case "sex":
        filterData = {
          sex: this.state.sex,
          patientType: this.state.patientType,
          illness: this.state.illness,
        };
        result = await this.props.sexFilter(filterData);
        this.setState({ result: result });
        break;
      case "municipality":
        filterData = {
          municipality: this.state.municipality,
          patientType: this.state.patientType,
          illness: this.state.illness,
        };
        result = await this.props.municipalityFilter(filterData);
        this.setState({ result: result });
        break;
      case "age":
        filterData = {
          min_age: this.state.min_age,
          max_age: this.state.max_age,
          patientType: this.state.patientType,
          illness: this.state.illness,
        };
        result = await this.props.ageFilter(filterData);
        this.setState({ result: result });
        break;
      case "month":
        filterData = {
          month: this.state.month,
          patientType: this.state.patientType,
          illness: this.state.illness,
        };
        result = await this.props.monthFilter(filterData);
        this.setState({ result: result });
        break;
      case "year":
        filterData = {
          year: this.state.year,
          patientType: this.state.patientType,
          illness: this.state.illness,
        };
        result = await this.props.yearFilter(filterData);
        this.setState({ result: result });
        break;
      default:
        break;
    }
    console.log(this.state.result);
  };

  render() {
    const { error } = this.state;
    let illnessContent;
    if (this.state.option !== "global") {
      illnessContent = (
        <Col className="form">
          <Form.Group controlId="illness">
            <Form.Label>Illness (Optional)</Form.Label>
            <Form.Control
              onChange={this.onChange}
              type="text"
              placeholder="Enter an illness"
            ></Form.Control>
          </Form.Group>
        </Col>
      );
    }
    let resultContent;
    let noResultContent;
    if (Object.keys(this.state.result).length !== 0) {
      let key = Object.keys(this.state.result)[0];
      if (this.state.result[key].length < 1) {
        noResultContent = (
          <div className="result-result">
            <h3>Results not found</h3>
          </div>
        );
      }
      switch (key) {
        case "Recovered":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Illness: {citizen.illness}</div>
              <div>Days to Recover: {citizen.length}</div>
              <div>Date of Recovery: {citizen.date}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Recovered_by_sex":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Sex: {citizen.sex}</div>
              <div>Illness: {citizen.illness}</div>
              <div>Days to Recover: {citizen.length}</div>
              <div>Date of Recovery: {citizen.date}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Recovered_by_age":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Age: {citizen.age}</div>
              <div>Illness: {citizen.illness}</div>
              <div>Days to Recover: {citizen.length}</div>
              <div>Date of Recovery: {citizen.date}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Recovered_by_month":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Illness: {citizen.illness}</div>
              <div>Days to Recover: {citizen.length}</div>
              <div>Date of Recovery: {citizen.date}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Recovered_by_year":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Illness: {citizen.illness}</div>
              <div>Days to Recover: {citizen.length}</div>
              <div>Date of Recovery: {citizen.date}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Recovered_by_municipality":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Municipality {citizen.municipality}</div>
              <div>Illness: {citizen.illness}</div>
              <div>Days to Recover: {citizen.length}</div>
              <div>Date of Recovery: {citizen.date}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Infected":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Illness: {citizen.infname}</div>
              <div>Date of Infection: {citizen.infdate}</div>
              <div>Number of times tested positive: {citizen.infcount}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Infected_by_age":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Age: {citizen.age}</div>
              <div>Illness: {citizen.infname}</div>
              <div>Date of Infection: {citizen.infdate}</div>
              <div>Number of times tested positive: {citizen.infcount}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Infected_by_municipality":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Municipality: {citizen.municipality}</div>
              <div>Illness: {citizen.infname}</div>
              <div>Date of Infection: {citizen.infdate}</div>
              <div>Number of times tested positive: {citizen.infcount}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Infected_by_sex":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Sex: {citizen.sex}</div>
              <div>Illness: {citizen.infname}</div>
              <div>Date of Infection: {citizen.infdate}</div>
              <div>Number of times tested positive: {citizen.infcount}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Infected_by_month":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Illness: {citizen.infname}</div>
              <div>Date of Infection: {citizen.infdate}</div>
              <div>Number of times tested positive: {citizen.infcount}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        case "Infected_by_year":
          resultContent = this.state.result[key].map((citizen) => (
            <div className="result-result">
              <h5>Citizen: {citizen.cid}</h5>
              <div>Illness: {citizen.infname}</div>
              <div>Date of Infection: {citizen.infdate}</div>
              <div>Number of times tested positive: {citizen.infcount}</div>
              <div
                style={{
                  borderTop: "1px solid #000000",
                  height: "1px",
                  marginBottom: "16px",
                }}
              ></div>
            </div>
          ));
          break;
        default:
          break;
      }
    }
    let additionalContent;
    switch (this.state.option) {
      case "sex":
        additionalContent = (
          <Col className="form-col-stats">
            <Form.Group controlId="sex">
              <Form.Label>Sex</Form.Label>
              <Form.Control
                onChange={this.onChange}
                value={this.state.sex}
                as="select"
                custom
                required
                placeholder="Choose Sex"
              >
                <option value="m">Male</option>
                <option value="f">Female</option>
              </Form.Control>
            </Form.Group>
          </Col>
        );
        break;
      case "municipality":
        additionalContent = (
          <Col className="form-col-stats">
            <Form.Group controlId="municipality">
              <Form.Label>Municipality</Form.Label>
              <Form.Control
                onChange={this.onChange}
                value={this.state.municipality}
                placeholder="Enter a municipality"
                type="text"
                required
              ></Form.Control>
            </Form.Group>
          </Col>
        );
        break;
      case "age":
        additionalContent = (
          <Col className="form-col-stats">
            <Form.Group controlId="min_age">
              <Form.Label>Minimum Age</Form.Label>
              <Form.Control
                onChange={this.onChange}
                value={this.state.min_age}
                placeholder="From"
                type="number"
                min="0"
                max="100"
                pattern="[0-9]*"
                isInvalid={error.age}
                required
              ></Form.Control>
              <Form.Control.Feedback type="invalid">
                {error.age}
              </Form.Control.Feedback>
            </Form.Group>
            <Form.Group controlId="max_age">
              <Form.Label>Max Age</Form.Label>
              <Form.Control
                onChange={this.onChange}
                value={this.state.max_age}
                placeholder="To"
                type="number"
                min="0"
                max="100"
                pattern="[0-9]*"
                isInvalid={error.age}
                required
              ></Form.Control>
              <Form.Control.Feedback type="invalid">
                {error.age}
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
        );
        break;
      case "month":
        additionalContent = (
          <Col className="form-col-stats">
            <Form.Group controlId="month">
              <Form.Label>Month</Form.Label>
              <Form.Control
                onChange={this.onChange}
                value={this.state.month}
                placeholder="Choose a month"
                as="select"
                custom
                type="month"
                required
              >
                <option value="01">January</option>
                <option value="02">February</option>
                <option value="03">March</option>
                <option value="04">April</option>
                <option value="05">May</option>
                <option value="06">June</option>
                <option value="07">July</option>
                <option value="08">August</option>
                <option value="09">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>
              </Form.Control>
            </Form.Group>
          </Col>
        );
        break;
      case "year":
        additionalContent = (
          <Col className="form-col-stats">
            <Form.Group controlId="year">
              <Form.Label>Year</Form.Label>
              <Form.Control
                onChange={this.onChange}
                value={this.state.year}
                placeholder="Enter in YYYY format"
                type="text"
                required
              ></Form.Control>
            </Form.Group>
          </Col>
        );
        break;
      default:
        break;
    }
    return (
      <div className="content-stats">
        <Container className="form-container-stats">
          <Form onSubmit={this.onSubmit}>
            <div style={{ marginTop: "20px", backgroundColor: "white" }}>
              <b>Find all sorts of information using our API</b>
            </div>
            <Row className="form-row-stats">
              <Col className="form-col-stats">
                <Form.Group controlId="patientType">
                  <Form.Label>Patient Type</Form.Label>
                  <Form.Control
                    onChange={this.onChange}
                    as="select"
                    custom
                    placeholder="Select type"
                    required
                  >
                    <option value="infected">Infected</option>
                    <option value="recovered">Recovered</option>
                  </Form.Control>
                </Form.Group>
              </Col>
              <Col className="form-col-stats">
                <Form.Group controlId="option">
                  <Form.Label>Filter</Form.Label>
                  <Form.Control
                    onChange={this.onChange}
                    as="select"
                    custom
                    placeholder="Select type"
                    required
                  >
                    <option value="global">Global</option>
                    <option value="sex">Sex</option>
                    <option value="municipality">Municipality</option>
                    <option value="age">Age</option>
                    <option value="month">Month</option>
                    <option value="year">Year</option>
                  </Form.Control>
                </Form.Group>
              </Col>
              {illnessContent}
              {additionalContent}
              <Col className="form-col-stats" style={{ paddingTop: "50px" }}>
                <Button
                  style={{ width: "80px" }}
                  variant="primary"
                  type="submit"
                  block
                >
                  Submit
                </Button>
              </Col>
            </Row>
          </Form>
        </Container>
        <div className="result-content">
          <div className="result-title">
            <h3>Results of your Search</h3>
          </div>
          {noResultContent}
          {resultContent}
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  error: state.error,
});

export default connect(mapStateToProps, {
  globalFilter,
  ageFilter,
  municipalityFilter,
  sexFilter,
  monthFilter,
  yearFilter,
})(Statistics);

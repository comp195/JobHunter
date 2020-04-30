import React from "react";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import CardMedia from "@material-ui/core/CardMedia";
import indeedImg from "../img/indeed.jpg";
import monsterImg from "../img/monster.jpg";

export default function JobCard({ jobData }) {
  const StylesCard = {
    backgroundColor: "#e6e6fa",
    margin: "1%",
    marginLeft: "28%",
    color: "black",
    border: "3px solid #e1e1f9",
    width: "45%",
  };

  return jobData.map(({ Title, Company, Location, Link, JobSource }) => (
    <Card justify="center" style={StylesCard}>
      <CardMedia
        component="img"
        height="70"
        image={JobSource === " Indeed" ? indeedImg : monsterImg}
        alt={JobSource === " Indeed" ? "Indeed" : "Monster"}
        title={JobSource === " Indeed" ? "Indeed" : "Monster"}
      />
      <CardContent>
        <Typography variant="h4" gutterBottom fontWeight="bold">
          {Title}
        </Typography>
        <Typography variant="h6" gutterBottom>
          {Company}
        </Typography>
        <Typography variant="h6" gutterBottom>
          {Location}
        </Typography>
        <Typography variant="h6" gutterBottom>
          Pulled from {JobSource}.com
        </Typography>
        <Button href={Link}>Click Here for this Job Posting</Button>
      </CardContent>
    </Card>
  ));
}

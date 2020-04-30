import React from "react";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
// import { makeStyles } from "@material-ui/core";

// const useStyles = makeStyles((theme) => ({
//   card: {},
// }));

export default function JobCard({ jobData, color }) {
  const indeedStylesCard = {
    borderColor:"Blue",
    backgroundColor: "#e6e6fa",
    margin: "0.5%",
    color: "black",
  };
  const monsterStylesCard = {
    borderColor: "Red"
    backgroundColor: "#e6e6fa",
    margin: "0.5%",
    color: "black",
  };

  return jobData.map(({ Title, Company, Location, Link, WebsiteName }) => (
    <Card
      style={
        { WebsiteName } === "Indeed" ? indeedStylesCard : monsterStylesCard
      }
    >
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
      </CardContent>
      <CardActions>
        <Button size="small" href={Link}>
          Click Here for this Job Posting
        </Button>
      </CardActions>
    </Card>
  ));
}

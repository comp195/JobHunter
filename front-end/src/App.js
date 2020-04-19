import React from "react";
import { Container, Box } from "@material-ui/core/";
import SlideOutMenu from "./SlideOutMenu";
import JobCard from "./JobCard";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles(theme => ({
  background: {
    // backgroundColor: ""
  },
  bar: {
    // backgroundColor: "#e6e6fa"
  }
}));

function App() {
  const styles = useStyles();
  return (
    <Box className={styles.background}>
      <Box className={styles.bar}>
        <SlideOutMenu />
      </Box>
      <Box>
        <Typography gutterBottom variant="h1" align="center" color="inherit">
          Job Finder
        </Typography>
        <Container>
          <JobCard />
          <JobCard />
          <JobCard />
          <JobCard />
          <JobCard />
          <JobCard />
          <JobCard />
        </Container>
      </Box>
    </Box>
  );
}

export default App;

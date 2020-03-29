import React from "react";
import { Button, Container, Box } from "@material-ui/core/";
import SlideOutMenu from "./SlideOutMenu";

function App() {
  return (
    <Container>
      <Box bgcolor="gray">
        <SlideOutMenu />
      </Box>
      <Box color="black" bgcolor="white">
        <h1>JobHunter</h1>
        <Button color="primary" variant="contained">
          Get Started
        </Button>
      </Box>
    </Container>
  );
}

export default App;

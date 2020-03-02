import React from "react";
import { Button, Box } from "@material-ui/core/";
import SlideOutMenu from "./SlideOutMenu";

function App() {
  return (
    <Box>
      <SlideOutMenu />
      <h1>JobHunter</h1>
      <Button color="primary" variant="contained">
        Get Started
      </Button>
    </Box>
  );
}

export default App;

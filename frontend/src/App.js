import React from 'react'; 
import Image from './components/Image.jsx'; 
import HSV from './components/HSV.jsx';

function App() {
  return ( 
    <body style={{background: "#808080", height: "100vh"}}>
      <div> 
        <div style={{background: "#FFFFFF"}}>
          <h1> Color Analyzer </h1>
          <h2> Sarah Dunbar, Roulettech Round 1 Interview </h2>
        </div>
        <div style={{display: "flex"}}>
          <Image />
          <HSV />
        </div>
      </div> 
    </body>
  ); 
}

export default App;

import React, { useState} from 'react'; 
import axios from "axios";
 
const HSV = () => { 
    const [hue, setHue] = useState();
    const [saturation, setSaturation] = useState();
    const [value, setValue] = useState();
    const [colorRender, setColorRender] = useState();
    const [splits, setSplits] = useState();
    const [hsv, setHSV] = useState();
    const [hex, setHex] = useState();

    const handleHSVSubmit = (e) => {
        e.preventDefault();
        let hsvData = new FormData();
        hsvData.set("hue", hue);
        hsvData.set("saturation", saturation);
        hsvData.set("value", value);
        axios.post('http://127.0.0.1:8000/api/hsv/', hsvData, {
          headers: {
            'content-type': 'multipart/form-data'
          }
        }).then(res => {
          let data = res.data;
          setColorRender(data[0]);
          setSplits(data[1]);
        })
        .catch(err => console.log(err))
      };
    
    const handleHueChange = (e) => {
      setHue(e.target.value);
      setColorRender(null);
      setSplits(null);
      setHSV(null);
      setHex(null);
    }

    const handleSaturationChange = (e) => {
      setSaturation(e.target.value);
      setColorRender(null);
      setSplits(null);
      setHSV(null);
      setHex(null);
    }

    const handleValueChange = (e) => {
      setValue(e.target.value);
      setColorRender(null);
      setSplits(null);
      setHSV(null);
      setHex(null);
    }

    function setHSVState(e, hex, hsv_code) {
      let hsv_polished = [Math.round(hsv_code[0]).toString() + " ", Math.round(hsv_code[1]).toString() + " ", Math.round(hsv_code[2])]
      setHSV(hsv_polished);
      setHex(hex);
    }

    function createColorDiv(split) {
      return <div> {split.map((entry) => <div style={{background : entry[0], height : (1 / split.length) * 200, width: 50}} onClick={(e) => setHSVState(e, entry[0], entry[1])}> </div>)} </div>
    }

    let colors;
    if (splits != null) {
      colors = <div style={{display: "flex"}}> {splits.map((split) => createColorDiv(split))} </div>
    }

    let colorBlock;
    if (colorRender != null) {
      colorBlock = <div style={{background : colorRender, height: 100, width: 200}}></div>
    }

    let hsvObj;
    if (hsv != null) {
      hsvObj = <p> { hex } { hsv } </p>
    }

    return (
        <div>
            <p> OR provide the hue, saturation, and value of a color for analysis </p>
            <form onSubmit={handleHSVSubmit}>
                <input type="number" step="1" placeholder='Hue' id='hue' required min="0" max="255" onChange={handleHueChange}/>
                <input type="number" step="1" placeholder='Saturation' id='saturation' required min="0" max="255" onChange={handleSaturationChange}/>
                <input type="number" step="1" placeholder='Value' id='value' required min="0" max="255" onChange={handleValueChange}/>
                <input type="submit" />
            </form>
            { colorBlock }
            { colors }
            { hsvObj }
        </div>
    );
}; 
 
export default HSV; 
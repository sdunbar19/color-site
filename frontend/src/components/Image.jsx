import React, { useState } from 'react'; 
import axios from "axios";

const Image = () => { 
  const [file, setFile] = useState();
  const [data, setData] = useState({});
  const [hex, setHex] = useState();
  const [hsv, setHSV] = useState();
  const [message, setMessage] = useState();

  const handleImageSubmit = (e) => {
    e.preventDefault();
    let imageData = new FormData();
    imageData.set("image", file);
    setMessage("Loading, please be patient!")
    axios.post('http://127.0.0.1:8000/api/image/', imageData, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }).then(res => {
      setMessage(null);
      setData(res.data['data']);
    })
    .catch(err => console.log(err))
  };

  const handleImageChange = (e) => {
    setData(null);
    setFile(e.target.files[0]);
    setHSV(null);
    setHex(null);
  }

  function setHSVState(e, hex, hsv_code) {
    let hsv_polished = [Math.round(hsv_code[0]).toString() + " ", Math.round(hsv_code[1]).toString() + " ", Math.round(hsv_code[2])]
    setHSV(hsv_polished);
    setHex(hex);
  }

  function createColorDiv(key, value) {
    return <div> {value.map((entry) => <div style={{background : entry[0], height : (entry[2] / entry[3]) * 200, width: 50}} onClick={(e) => setHSVState(e, entry[0], entry[1])}> </div>)} </div>
  }

  let renderedImage;
  if (file != null) {
    renderedImage = <img src={URL.createObjectURL(file)} alt="user-uploaded" style={{height: 300}}></img>;
  }


  let colors;
  if (data != null) {
    colors = <div style={{display: "flex"}}> {Object.entries(data).map(([key, value]) => createColorDiv(key, value))} </div>
  }

  let hsvObj;
  if (hsv != null) {
    hsvObj = <p> { hex } { hsv } </p>
  }

  return ( 
    <div>
      <p> Upload an image for analysis </p>
      <form onSubmit={handleImageSubmit}>
        <input type="submit" />
        <label for="image"> Image: </label>
        <input type="file"
                id="image"
                accept="image/png, image/jpeg" 
                onChange={handleImageChange}
                required/>
      </form>
      { renderedImage }
      <p> { message } </p>
      { colors }
      { hsvObj }
    </div> 
  ); 
}; 
 
export default Image; 
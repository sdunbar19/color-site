import React, { useState } from 'react'; 
import axios from "axios";

const COLOR_DIV_HEIGHT = 200
const COLOR_DIV_WIDTH = 25
const DJANGO_URL = 'http://127.0.0.1:8000/api/image/'

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
    axios.post(DJANGO_URL, imageData, {
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
    return (
      <div> 
        {value.map((entry) => <div style={{background : entry[0], height : (entry[2] / entry[3]) * COLOR_DIV_HEIGHT, width: COLOR_DIV_WIDTH}} 
                                   onClick={(e) => setHSVState(e, entry[0], entry[1])}> </div>)} 
      </div>
    );
  }

  let renderedImage;
  if (file != null) {
    renderedImage = <img src={URL.createObjectURL(file)} alt="user-uploaded" style={{height: COLOR_DIV_HEIGHT}}></img>;
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
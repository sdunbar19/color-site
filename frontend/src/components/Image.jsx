import React, { useState } from 'react'; 
import axios from "axios";

const Image = () => { 
  const [color, setColor] = useState("#FFFFFF");
  const [file, setFile] = useState();

  const handleImageSubmit = (e) => {
    e.preventDefault();
    let imageData = new FormData();
    imageData.set("image", file);
    console.log(imageData.get("image"));
    axios.post('http://127.0.0.1:8000/api/image/', imageData, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }).then(res => {
      let data = res.data['data'];
      setColor(data);
    })
    .catch(err => console.log(err))
  };

  const handleImageChange = (e) => {
    setColor("#FFFFFF");
    setFile(e.target.files[0]);
  }

  let renderedImage;
  if (file != null) {
    renderedImage = <img src={URL.createObjectURL(file)} alt="user-uploaded" style={{height: 300}}></img>;
  }

  return ( 
    <div>
      <p> Upload an image for analysis </p>
      <form onSubmit={handleImageSubmit}>
        <label for="image"> Image: </label>
        <input type="file"
                id="image"
                accept="image/png, image/jpeg" 
                onChange={handleImageChange}
                required/>
        <input type="submit" />
      </form>
      { renderedImage }
      <div id="results" style={{background : color, height : 100}}></div>
    </div> 
  ); 
}; 
 
export default Image; 
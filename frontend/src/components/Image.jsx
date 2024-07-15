import React, { Component } from 'react'; 
import axios from "axios";

class Image extends Component { 
  imageData = new FormData();

  handleImageSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/image/', this.imageData, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }).then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err))
  };

  handleImageChange = (e) => {
    console.log(e)
    this.imageData.set("image", e.target.files[0])
  }

  render() { 
    return ( 
      <div>
        <p> Upload an image for analysis </p>
        <form onSubmit={this.handleImageSubmit}>
          <label for="image"> Image: </label>
          <input type="file"
                 id="image"
                 accept="image/png, image/jpeg" 
                 onChange={this.handleImageChange}
                 required/>
          <input type="submit" />
        </form>
      </div> 
    );
  } 
}; 
 
export default Image; 
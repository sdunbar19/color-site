import React, { Component } from 'react'; 
import axios from "axios";
 
class HSV extends Component { 
    hsvData = new FormData();

    handleHSVSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/hsv/', this.hsvData, {
          headers: {
            'content-type': 'multipart/form-data'
          }
        }).then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
      };
    
    handleHueChange = (e) => {
        this.hsvData.set("hue", e.target.value)
    }

    handleSaturationChange = (e) => {
        this.hsvData.set("saturation", e.target.value)
    }

    handleValueChange = (e) => {
        this.hsvData.set("value", e.target.value)
    }

    render() {
        return (
            <div>
                <p> OR provide the hue, saturation, and value of a color for analysis </p>
                <form onSubmit={this.handleHSVSubmit}>
                    <input type="number" step="1" placeholder='Hue' id='hue' required min="0" max="255" onChange={this.handleHueChange}/>
                    <input type="number" step="1" placeholder='Saturation' id='saturation' required min="0" max="255" onChange={this.handleSaturationChange}/>
                    <input type="number" step="1" placeholder='Value' id='value' required min="0" max="255" onChange={this.handleValueChange}/>
                    <input type="submit" />
                </form>
            </div>
        );
    }
}; 
 
export default HSV; 
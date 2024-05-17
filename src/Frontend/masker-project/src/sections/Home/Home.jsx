import React from "react";
import "./Home.css"
import PhotoDisplay from "../../components/PhotoDisplay/PhotoDisplay";


function Home(){
    return (
        <div className="Home">
            <h1 id="title-label">MASKER</h1>
            <div className="photodisplay-container">
                <PhotoDisplay filterName={"Original"}>
                    <button>SNAP</button>
                </PhotoDisplay>
                <PhotoDisplay filterName={"Test"}>
                    <button>SNAP</button>
                </PhotoDisplay>
            </div>
            <h3>Filter</h3>
            <select>
                <option value="remove-background">remove background</option>
                <option value="filter-silhouette">silhouete</option>
            </select>
            
        </div>
    )
}


export default Home
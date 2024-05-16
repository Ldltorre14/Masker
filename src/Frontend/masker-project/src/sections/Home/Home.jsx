import React from "react";
import "./Home.css"
import PhotoDisplay from "../../components/PhotoDisplay/PhotoDisplay";
import Button from "../../components/Button/Button";

function Home(){
    return (
        <div className="Home">
            <h1 id="title-label">MASKER</h1>
            <div className="filter-label-container">
                <h2>Original</h2>
                <h2>Filter</h2>
            </div>
            <div className="photodisplay-container">
                <PhotoDisplay />
                <PhotoDisplay />
            </div>
            <div className="button-container">
                <Button />
            </div>
            
        </div>
    )
}


export default Home
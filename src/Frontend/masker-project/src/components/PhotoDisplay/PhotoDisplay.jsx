import React, {useEffect, useRef} from "react";
import WebCam from "../WebCam/WebCam";
import "./PhotoDisplay.css"

function PhotoDisplay({filterName, children}){
    const videoRef = useRef(null)


    return(
        <div className="frame">
            <h2>{filterName}</h2>
            <WebCam />
            {children}
        </div>
    )
    
}



export default PhotoDisplay
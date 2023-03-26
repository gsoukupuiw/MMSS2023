import React from "react";
import {FaGithub} from "react-icons/fa";
import './App.css'

export default function App() {
  return (
    <>
  <div className="relative overflow-hidden bg-slate-900 py-6 sm:py-12">

    <h1 className="text-3xl text-center font-semibold text-slate-100"> Geo Cache Game</h1>
    <p className="text-xl text-center font-normal text-emerald-700 italic"> Into The Unknown</p>

  </div>

  <div className="flex justify-center items-center h-screen">
  <div className="flex flex-col">
     <input type="text" placeholder="Enter your text" class="border-2 border-gray-300 py-2 px-4 rounded-md"></input>
  <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-10"> 
    Sign in
  </button>
  </div>
  
</div>

      
  <div className="relative overflow-hidden bg-amber-700 py-6 sm:py-12">
    
    <h1 className="text-center text-3xl font-semibold text-slate-100">Contributors</h1>
    <div className="space-between justify-center">
      <p className="text-slate-100 flex flex-col space-y-4 space-x-4">
        <FaGithub size={28}/>
        <FaGithub size={28}/>
        <FaGithub size={28}/>
        <FaGithub size={28}/>
      </p>
      
    </div>
    <p className="text-center text-xl font-normal italic text-emerald-800">Into The Unknown</p>
  </div>

  </>
  )
}

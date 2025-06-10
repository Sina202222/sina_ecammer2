import type { ComponentProps } from "react"

type Variant=  "primary" | "secondary" | "danger" | "warning" | "success" ;

type Button= ComponentProps<"button"> & {
    variant?: Variant
}
function Button({children, variant, style, className, ...rest}: Button) {
    // console.log(checkVariant(variant))

    return (
        <button {...rest} className= {className} style={{ borderRadius: "16px", padding:"14px ", ...style, ...checkVariant(variant)}} > {children}</button>
    )
}

export default Button

function checkVariant(variant?: Variant){
   
    switch (variant) {
        case "primary":
          return { backgroundColor: "blue", color: "white" };
        case "secondary":
          return { backgroundColor: "gray", color: "black" };
        case "danger":
          return { backgroundColor: "red", color: "white" };
        case "success":
            return { backgroundColor: "green", color: "white" };
        default:
          return {};
      }
   
   
    // if (variant === "primary"){
    //     return {backgroundColor: "blue", color: "white"};
    // } 
    // else if (variant === "secondary") {
    //     return { backgroundColor: "gray", color: "black"}
    // } 
    // else if (variant === "danger") {
    //     return { backgroundColor: "red", color: "white"}
    // }
    //  else if (variant === "success") {
    //     return { backgroundColor: "green", color: "black"}
    // }
  
}
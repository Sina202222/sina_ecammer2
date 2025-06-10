
import { Link } from 'react-router-dom';
import Container from "../container/Container";
import Button from '../button/Button';

function Navbar() {
      
    const hb = {
        
        borderBottomWidth: '1px', /* border-b */
        boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06)', /* shadow */
    
      }

    


    return (

    <section className='h-14 border-b shadow flex items-center  ' style={hb}> 
        <Container>
                <div className='flex justify-between flex-row-reverse  ' >
                    <ul className='flex flex-row-reverse m-8'  >
                        <li className=' ml-4'>
                            <Link to="/store " className=' ' >فروشگاه</Link>
                        </li>
                        <li className=' ml-4 ' >
                            <Link to="/" className='' >خانه</Link>
                        </li>
                    </ul>

                    <div className='m-6'>
                        <Button > خارج شدن </Button>
                        <Link className='relative' to="/cart">
                            <button className='rounded-full  p-2 '>  
                                <svg xmlns="http://www.w3.org/2000/svg" width="27" height="27" fill="currentColor" className="bi bi-basket" viewBox="0 0 16 16">
                                 <path d="M5.757 1.071a.5.5 0 0 1 .172.686L3.383 6h9.234L10.07 1.757a.5.5 0 1 1 .858-.514L13.783 6H15a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1v4.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 13.5V9a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h1.217L5.07 1.243a.5.5 0 0 1 .686-.172zM2 9v4.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V9zM1 7v1h14V7zm3 3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3A.5.5 0 0 1 4 10m2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3A.5.5 0 0 1 6 10m2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3A.5.5 0 0 1 8 10m2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3a.5.5 0 0 1 .5-.5m2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3a.5.5 0 0 1 .5-.5"/>
                                </svg>
                            </button>
                            <span className='absolute w-5 h-6 bg-red-400  justify-center items-center text-white rounded-full  mt-2  '> 
                               
                            </span>
                        </Link>
                    </div>
                </div>
        </Container>

    </section>

    

  )
}

export default Navbar
/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Box, HStack, Image as ChakraImage, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Box>
  <VStack sx={{"bg": "#212529", "position": "sticky", "borderBottom": "0.25em solid #D3D3D3", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0", "width": "100%"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`moredev`} src={`https://adviento.dev/mouredev.png`} sx={{"width": "4em", "height": "4em"}}/>
  <Text>
  {`aDEViento 2023`}
</Text>
  <Spacer/>
</HStack>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Calendario de aDEViento 2023 | 24 días. 24 regalos.`}
</title>
  <meta content={`Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra comunidad de developers! Una actividad en la que cada día sortearé un regalo relacionado con programación y desarrollo de software (libros, cursos…). Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje en comunidad.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}

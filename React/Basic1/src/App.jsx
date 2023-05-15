import { ThemeProvider, styled } from "styled-components";
import { GlobalStyle } from "./style/globalStyle";
import { theme } from "./style/theme";
import CardsPage from "./@pages/cardsPage";

export default function App() {
  return (
    <>
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        <CardsPage/>
      </ThemeProvider>
    </>
  );
}

const Title = styled.h1`
  ${({ theme }) => theme.fonts.title}
`;
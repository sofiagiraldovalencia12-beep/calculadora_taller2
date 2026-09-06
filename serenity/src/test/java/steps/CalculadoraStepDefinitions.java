package steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import io.restassured.response.Response;
import net.serenitybdd.rest.SerenityRest;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

/**
 * Step definitions de Serenity BDD (Paso 6 del taller).
 * Estas pruebas E2E llaman a la API REST real (los endpoints de FastAPI)
 * y validan el comportamiento desde la perspectiva del usuario final.
 *
 * Requiere que la API esté corriendo, por ejemplo:
 *   uvicorn app.main:app --reload
 */
public class CalculadoraStepDefinitions {

    private static final String BASE_URL = "http://127.0.0.1:8000";

    private double numeroA;
    private double numeroB;
    private Response respuesta;

    @Given("que tengo los números {double} y {double}")
    public void queTengoLosNumeros(double a, double b) {
        this.numeroA = a;
        this.numeroB = b;
    }

    @When("sumo ambos números")
    public void sumoAmbosNumeros() {
        respuesta = llamarEndpoint("/sumar");
    }

    @When("resto el segundo del primero")
    public void restoElSegundoDelPrimero() {
        respuesta = llamarEndpoint("/restar");
    }

    @When("multiplico ambos números")
    public void multiplicoAmbosNumeros() {
        respuesta = llamarEndpoint("/multiplicar");
    }

    @When("divido el primero entre el segundo")
    public void dividoElPrimeroEntreElSegundo() {
        respuesta = llamarEndpoint("/dividir");
    }

    @Then("el resultado debe ser {double}")
    public void elResultadoDebeSer(double resultadoEsperado) {
        respuesta.then().statusCode(200);
        assertThat(respuesta.jsonPath().getDouble("resultado"), equalTo(resultadoEsperado));
    }

    @Then("debo recibir un error indicando que no se puede dividir entre cero")
    public void deboRecibirUnErrorDeDivisionEntreCero() {
        respuesta.then().statusCode(400);
    }

    private Response llamarEndpoint(String path) {
        return SerenityRest
                .given()
                .contentType("application/json")
                .body("{\"a\": " + numeroA + ", \"b\": " + numeroB + "}")
                .when()
                .post(BASE_URL + path);
    }
}

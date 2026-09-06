package runners;

import io.cucumber.junit.CucumberOptions;
import net.serenitybdd.cucumber.CucumberWithSerenity;
import org.junit.runner.RunWith;

@RunWith(CucumberWithSerenity.class)
@CucumberOptions(
        features = "src/test/resources/features",
        glue = "steps"
)
public class CalculadoraTestSuite {
    // Clase vacía: solo sirve como punto de entrada para ejecutar los .feature
}

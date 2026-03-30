# TODO: Fix Java Calculator Project Errors

## Steps from approved plan (progress tracked):

### 1. Update pom.xml [DONE]
   - Add JUnit Jupiter dependency
   - Update Java compiler version to 21

### 2. Update Calculator.java [DONE]
   - Add int overloads for add, subtract, multiply, divide

### 3. Fix CalculatorTest.java [DONE]
   - Correct package declaration to com.devops
   - Fix import path for Calculator
   - Add static import for Assertions
   - Update tests to use int methods

### 4. Delete duplicate Test.java [DONE]
   - Renamed to Test-deleted.txt (manual delete recommended)

### 5. Fix ci.yml [DONE]
   - Added proper Maven CI workflow

### 6. Verify with Maven [TODO]
   - Run `mvn clean compile test`

**Next step: 6/6 - Verify**

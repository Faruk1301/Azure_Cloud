resource "azurerm_resource_group" "rg" {
  name     = "RG3"
  location = "East US"

  tags = {
    environment = "development"
    department  = "IT"
  }
}





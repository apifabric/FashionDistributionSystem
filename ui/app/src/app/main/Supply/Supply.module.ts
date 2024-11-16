import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUPPLY_MODULE_DECLARATIONS, SupplyRoutingModule} from  './Supply-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SupplyRoutingModule
  ],
  declarations: SUPPLY_MODULE_DECLARATIONS,
  exports: SUPPLY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SupplyModule { }
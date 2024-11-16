import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {COLLECTION_MODULE_DECLARATIONS, CollectionRoutingModule} from  './Collection-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CollectionRoutingModule
  ],
  declarations: COLLECTION_MODULE_DECLARATIONS,
  exports: COLLECTION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CollectionModule { }
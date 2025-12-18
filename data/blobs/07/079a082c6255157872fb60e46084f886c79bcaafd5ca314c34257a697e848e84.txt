package manager;

/**
 * An abstract class that represents all types of properties.
 * 
 * @author mdixon, Garima Dhakal
 *
 */
abstract class Property {

	private String address; //Address of Property.
	private Tenant tenant; //tenant of property.
	
	/**
	 * 
	 * @return the property address.
	 */
	public String getAddress() { //Gets the propery address.
		
		return address;
	}
	
	/**
	 * Sets the tenant of the property.
	 * 
	 * @param tenant the tenant of the property
	 */
	public void setTenant(Tenant tenant) {
		
		this.tenant=tenant;
	}
	
	/**
	 * Removes any tenant from the property.
	 */
	public void removeTenant() {
		
		tenant=null;
	}
	
	/**
	 * 
	 * @return true if the property has a tenant
	 */
	public boolean hasTenant() {
		
		return (tenant!=null);
	}
	
	/**
	 * Parameterized Constructor
	 * 
	 * @param address the property address.
	 */
	Property(String address) {
		
		this.address=address;
	}
	
}
